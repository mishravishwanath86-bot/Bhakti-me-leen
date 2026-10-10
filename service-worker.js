// service-worker.js - Complete unregistration and cache wipeout
self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(keys.map(k => caches.delete(k)));
    }).then(() => {
      return self.registration.unregister();
    }).then(() => {
      return clients.claim();
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(fetch(event.request));
});
