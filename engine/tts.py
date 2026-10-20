import json, re, subprocess, sys, os, numpy as np, onnxruntime as ort, wave
H=os.path.dirname(os.path.abspath(__file__))
vocab=json.load(open(f'{H}/src/src/kokoro_onnx/config.json'))['vocab']
voices=np.load(f'{H}/voices.bin')
sess=ort.InferenceSession(f'{H}/kokoro.onnx',providers=['CPUExecutionProvider'])
inames=[i.name for i in sess.get_inputs()]; tokname='input_ids' if 'input_ids' in inames else 'tokens'
sp_dtype=[i for i in sess.get_inputs() if i.name=='speed'][0].type
def ipa(chunk):
    env=dict(os.environ,LD_LIBRARY_PATH=f'{H}/piper')
    out=subprocess.run([f'{H}/piper/espeak-ng',f'--path={H}/piper/espeak-ng-data','-v','pt-br','-q','--ipa'],input=chunk,capture_output=True,text=True,env=env).stdout
    return ' '.join(out.split())
def phonemize(text):
    parts=re.split(r'([,.;:!?])',text); res=''
    for p in parts:
        if not p.strip(): continue
        if p in ',.;:!?': res=res.rstrip()+p+' '
        else: res+=ipa(p)+' '
    return ''.join(c for c in res.strip() if c in vocab)
def synth(text,voice,speed=1.0):
    ph=phonemize(text); toks=[vocab[c] for c in ph]
    st=voices[voice][min(len(toks),509)]
    sp=np.array([speed],dtype=np.int32 if 'int' in sp_dtype else np.float32)
    a=sess.run(None,{tokname:np.array([[0,*toks,0]],dtype=np.int64),'style':st.astype(np.float32),'speed':sp})[0].ravel()
    return ph,a
if __name__=='__main__':
    lines=json.load(open(sys.argv[1])); voice=sys.argv[2]; outdir=sys.argv[3]; speed=float(sys.argv[4]) if len(sys.argv)>4 else 1.0
    os.makedirs(outdir,exist_ok=True); meta=[]
    for i,t in enumerate(lines):
        ph,a=synth(t,voice,speed)
        # trim silence
        thr=0.01*np.abs(a).max(); idx=np.where(np.abs(a)>thr)[0]; a=a[max(0,idx[0]-600):idx[-1]+2400]
        a=(a/np.abs(a).max()*0.9*32767).astype('<i2')
        w=wave.open(f'{outdir}/l{i}.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000);w.writeframes(a.tobytes());w.close()
        meta.append({'i':i,'text':t,'dur':round(len(a)/24000,2),'ph':ph})
    json.dump(meta,open(f'{outdir}/meta.json','w'),ensure_ascii=False,indent=1)
    for m in meta: print(m['dur'],m['text'])
