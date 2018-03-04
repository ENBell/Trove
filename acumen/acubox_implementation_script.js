/* This script can be loaded on a remote page to call a Acumen url -> view -> template. */

var tag = document.createElement('script');
tag.src = 'http://127.0.0.1:8000/acubox';
/* tag.setAttribute('async','');*/
document.body.appendChild(tag);