// service-worker.js

self.addEventListener('install', function(event) {
    console.log('Service Worker: Installed');
  });
  
  self.addEventListener('activate', function(event) {
    console.log('Service Worker: Activated');
  });
  
  self.addEventListener('fetch', function(event) {
    // For now, this handles basic fetches but can be extended to cache or sync
    event.respondWith(fetch(event.request));
  });
  
  // Listen for push events for notifications
  self.addEventListener('push', function(event) {
    const data = event.data.json();
    console.log('Push received: ', data);
  
    // Display a notification
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: 'https://example.com/notification-icon.png'
    });
  });
      
