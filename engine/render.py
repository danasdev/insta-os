import sys, os, json
# Uso: python3 render.py stills 3.0 7.5 ...   |   python3 render.py full [quadro_ini] [quadro_fim]
# A pagina e definida por PAGE (padrao: exemplo-produto/index.html ao lado deste script) ou por URL (ex.: http://127.0.0.1:8765/index.html,
# necessario quando o template usa mask-image/fetch, que o navegador bloqueia em file://). ORIENT=portrait gera 1080x1920.
HERE=os.path.dirname(os.path.abspath(__file__))
URL=os.environ.get('URL') or 'file://'+os.path.abspath(os.environ.get('PAGE',os.path.join(HERE,'exemplo-produto','index.html')))
from playwright.sync_api import sync_playwright
mode=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(args=["--force-device-scale-factor=1"])
    P=os.environ.get('ORIENT')=='portrait'
    pg=b.new_page(viewport={'width':1080,'height':1920} if P else {'width':1920,'height':1080})
    FD='frames_p' if P else 'frames'; SD='stills_p' if P else 'stills'
    msgs=[]
    pg.on('console',lambda m:msgs.append(m.text)); pg.on('pageerror',lambda e:msgs.append('ERR '+str(e)))
    pg.goto(URL); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    if mode=='stills':
        os.makedirs(SD,exist_ok=True)
        for t in [float(x) for x in sys.argv[2:]]:
            pg.evaluate(f'seek({t})'); pg.screenshot(path=f'{SD}/t{t:06.2f}.jpg',type='jpeg',quality=85)
    else:
        os.makedirs(FD,exist_ok=True)
        fps=30; D=pg.evaluate('DURATION'); n=int(D*fps)
        a=int(sys.argv[2]) if len(sys.argv)>2 else 0; z=int(sys.argv[3]) if len(sys.argv)>3 else n
        for i in range(a,min(z,n)):
            pg.evaluate(f'seek({i/fps})'); pg.screenshot(path=f'{FD}/f{i:05d}.jpg',type='jpeg',quality=93)
    print('\n'.join(msgs[:10]))
    b.close()
