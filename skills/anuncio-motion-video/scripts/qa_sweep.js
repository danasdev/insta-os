// Varredura de QA: texto fora da tela e dentro da área segura do reel.
// Funciona em qualquer página com seek(t) e DURATION. Cole no console do navegador do Playwright
// (page.evaluate com o conteúdo deste arquivo) DEPOIS que as fontes carregarem:
//   await document.fonts.ready;  // e document.fonts.load("100px 'SuaFonteDeTitulo'") etc. para cada família usada
// Uso:  qaSweep({step:0.1})   → { portrait, issues:[...] }
//
// Regras:
//  - considera cada nó de texto visível (opacidade acumulada > 0.3, sem display:none/visibility:hidden);
//  - 'offscreen': o retângulo do texto sai de [0,W]x[0,H] (tolerância 2px);
//  - 'safe': (só em 9:16) o texto invade os 250px de cima/baixo ou os 120px da direita;
//  - ignora elementos com data-qa-ignore (ou dentro de um) — use para o que entra de fora de propósito,
//    para a marca d'água e para legendas queimadas que ficam por cima da área de UI de propósito;
//  - agrupa ocorrências consecutivas do mesmo texto/tipo em uma linha com tempo inicial e final.
(function () {
  function opacityOf(el) {
    var o = 1;
    for (var e = el; e && e !== document.documentElement; e = e.parentElement) {
      var cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.visibility === 'hidden') return 0;
      o *= parseFloat(cs.opacity);
    }
    return o;
  }
  function ignored(el) {
    return !!(el.closest && el.closest('[data-qa-ignore]'));
  }
  window.qaSweep = function (opts) {
    opts = opts || {};
    var step = opts.step || 0.1;
    var W = window.innerWidth, H = window.innerHeight;
    var portrait = H > W;
    var safe = Object.assign({ top: 250, bottom: 250, right: 120, left: 0 }, opts.safe || {});
    var tol = 2, issues = [], open = {};
    // `const DURATION` não vira propriedade de window: use o identificador global direto.
    var D = (typeof DURATION !== 'undefined') ? DURATION : window.DURATION;
    if (typeof D !== 'number' || !isFinite(D)) throw new Error('qaSweep: DURATION não encontrada (defina const DURATION = segundos)');
    if (typeof seek !== 'function') throw new Error('qaSweep: função seek(t) não encontrada');

    for (var t = 0; t <= D + 1e-6; t += step) {
      seek(t);
      var seen = {};
      var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      var node;
      while ((node = walker.nextNode())) {
        var txt = node.nodeValue.trim();
        if (!txt) continue;
        var el = node.parentElement;
        if (!el || ignored(el) || opacityOf(el) <= 0.3) continue;
        var tag = el.tagName;
        if (tag === 'SCRIPT' || tag === 'STYLE') continue;
        var range = document.createRange();
        range.selectNodeContents(node);
        var r = range.getBoundingClientRect();
        if (r.width < 1 || r.height < 1) continue;

        var kinds = [];
        if (r.left < -tol || r.top < -tol || r.right > W + tol || r.bottom > H + tol) kinds.push('offscreen');
        if (portrait && (r.top < safe.top || r.bottom > H - safe.bottom || r.right > W - safe.right || r.left < safe.left))
          kinds.push('safe');
        kinds.forEach(function (k) {
          var key = k + '|' + txt.slice(0, 40);
          seen[key] = { kind: k, text: txt.slice(0, 40), rect: [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)] };
        });
      }
      // fecha/abre ocorrências
      Object.keys(open).forEach(function (key) {
        if (!seen[key]) { open[key].to = +(t - step).toFixed(2); issues.push(open[key]); delete open[key]; }
      });
      Object.keys(seen).forEach(function (key) {
        if (!open[key]) open[key] = Object.assign({ from: +t.toFixed(2) }, seen[key]);
      });
    }
    Object.keys(open).forEach(function (key) { open[key].to = D; issues.push(open[key]); });
    return { portrait: portrait, size: [W, H], duration: D, count: issues.length, issues: issues };
  };
})();
