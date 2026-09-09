
(() => {
  const root = document.documentElement;
  const themeBtn = document.querySelector('[data-theme-toggle]');
  const fontBtn = document.querySelector('[data-font-toggle]');
  const favBtn = document.querySelector('[data-favorite]');
  const savedTheme = localStorage.getItem('yidian.theme');
  if(savedTheme) root.dataset.theme = savedTheme;

  const setThemeLabel = () => {
    if(!themeBtn) return;
    const t = root.dataset.theme || 'system';
    themeBtn.textContent = t === 'dark' ? '☾ 深色' : t === 'light' ? '☀ 浅色' : '◐ 系统';
  };
  setThemeLabel();

  themeBtn?.addEventListener('click', () => {
    const current = root.dataset.theme || 'system';
    const next = current === 'system' ? 'light' : current === 'light' ? 'dark' : 'system';
    if(next === 'system'){ delete root.dataset.theme; localStorage.removeItem('yidian.theme'); }
    else { root.dataset.theme = next; localStorage.setItem('yidian.theme', next); }
    setThemeLabel();
  });

  const sizes = ['16px','18px','20px'];
  let sizeIndex = Number(localStorage.getItem('yidian.fontIndex') || 1);
  root.style.setProperty('--font-size', sizes[sizeIndex]);
  const setFontLabel=()=>{if(fontBtn) fontBtn.textContent='Aa ' + ['小','标准','大'][sizeIndex]};
  setFontLabel();
  fontBtn?.addEventListener('click',()=>{
    sizeIndex=(sizeIndex+1)%sizes.length;
    root.style.setProperty('--font-size',sizes[sizeIndex]);
    localStorage.setItem('yidian.fontIndex',sizeIndex);
    setFontLabel();
  });

  const progress = document.querySelector('.article-progress');
  if(progress){
    const update=()=>{
      const h=document.documentElement;
      const max=h.scrollHeight-innerHeight;
      const pct=max>0?Math.min(100,scrollY/max*100):0;
      progress.style.width=pct+'%';
      if(pct>88 && document.body.dataset.articleId){
        const read=JSON.parse(localStorage.getItem('yidian.read')||'[]');
        if(!read.includes(document.body.dataset.articleId)){read.push(document.body.dataset.articleId);localStorage.setItem('yidian.read',JSON.stringify(read));}
      }
    };
    addEventListener('scroll',update,{passive:true});update();
  }

  if(favBtn && document.body.dataset.articleId){
    const id=document.body.dataset.articleId;
    const getFav=()=>JSON.parse(localStorage.getItem('yidian.favorites')||'[]');
    const paint=()=>favBtn.textContent=getFav().includes(id)?'★ 已收藏':'☆ 收藏';
    paint();
    favBtn.addEventListener('click',()=>{
      let fav=getFav();
      fav=fav.includes(id)?fav.filter(x=>x!==id):[...fav,id];
      localStorage.setItem('yidian.favorites',JSON.stringify(fav));paint();
    });
  }

  document.querySelectorAll('[data-quiz]').forEach(group=>{
    group.querySelectorAll('button').forEach(btn=>btn.addEventListener('click',()=>{
      const q=btn.closest('.quiz-q');
      q.querySelectorAll('button').forEach(b=>{
        b.disabled=true;
        if(b.dataset.correct==='true') b.classList.add('correct');
        else if(b===btn) b.classList.add('wrong');
      });
      q.querySelector('.explain').style.display='block';
    }));
  });

  const box=document.querySelector('.lightbox');
  document.querySelectorAll('.zoomable').forEach(img=>img.addEventListener('click',()=>{
    if(!box)return;
    box.querySelector('img').src=img.src;box.classList.add('open');
  }));
  box?.querySelector('button')?.addEventListener('click',()=>box.classList.remove('open'));
  box?.addEventListener('click',e=>{if(e.target===box)box.classList.remove('open')});
})();
