(function(){var d=document,io;
var n=d.querySelector('.nav');addEventListener('scroll',function(){n.classList.toggle('s',scrollY>8)},{passive:true});
if('IntersectionObserver'in window){io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});d.querySelectorAll('.r').forEach(function(el){io.observe(el)})}else d.querySelectorAll('.r').forEach(function(el){el.classList.add('in')});
var box=d.getElementById('vids');
if(box){box.addEventListener('click',function(e){var b=e.target.closest('.yt');if(!b)return;var f=d.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(b.dataset.id)+'?autoplay=1&playsinline=1&rel=0';f.title=b.dataset.title;f.allow='autoplay;encrypted-media;picture-in-picture';f.allowFullscreen=true;b.replaceWith(f)})}
d.querySelectorAll('video[data-src]').forEach(function(v){var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){v.src=v.dataset.src;o.disconnect()}});o.observe(v)});
var y=d.getElementById('y');if(y)y.textContent=new Date().getFullYear();})();
