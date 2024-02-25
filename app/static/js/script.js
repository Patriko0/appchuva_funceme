function OnclickMarker(marker) {
  const postID = marker.getAttribute('value')
  document.getElementById('inputId').value = postID;
}

const markers = document.querySelectorAll("gmp-advanced-marker")

markers.forEach((marker) => {
  marker.addEventListener('click', () => { OnclickMarker(marker) })
  
})