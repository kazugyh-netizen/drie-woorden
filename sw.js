// 圏外でも開けるように、アプリ一式を端末に置いておく。中身を変えたら VERSION を上げる。
const VERSION = 'dw-3';
const FILES = ['./', 'index.html', 'words.txt', 'ja_nl.txt', 'manifest.json', 'icon-180.png', 'icon-512.png'];
self.addEventListener('install', e => e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES)).then(() => self.skipWaiting())));
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())
));
// 先にネットを見て、つながらなければ手元の控えを出す
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request).then(r => {
      if (r.ok && new URL(e.request.url).origin === location.origin) caches.open(VERSION).then(c => c.put(e.request, r.clone()));
      return r;
    }).catch(() => caches.match(e.request, {ignoreSearch: true}))
  );
});
