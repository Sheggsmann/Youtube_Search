// function geolocate() {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(function(position) {
//             var geolocation = {
//                 lat: position.coords.latitude,
//                 lng: position.coords.longitude
//             };
//             var circle = new google.maps.Circle({
//                 center: geolocation,
//                 radius: position.coords.accuracy
//             });
//             autoComplete.setBounds(circle.getBounds());
//         });
//     }
// }