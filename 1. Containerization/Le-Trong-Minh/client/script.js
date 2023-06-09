window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


const web_url = 
      "http://localhost:5000";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
// Calling that async function
getapi(web_url);
  
// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
    let tab = 
        `<tr>
            <th>STT</th>
            <th>Họ và tên</th>
            <th>Năm sinh</th>
            <th>Giới tính</th>
            <th>Trường</th>
            <th>Chuyên ngành</th>
        </tr>`;
    
    // Loop to access all rows
    for (let r of data) {
        tab += `<tr>
    <td>${r.stt} </td>
    <td>${r.name} </td>
    <td>${r.birth}</td>
    <td>${r.sex}</td>
    <td>${r.university}</td> 
    <td>${r.major}</td>          
</tr>`;
    }
    // Setting innerHTML as tab variable
    document.getElementById("data").innerHTML = tab;
}