const searchBtn = document.querySelector('#search-btn');

searchBtn.onclick = function() {
    const id = document.querySelector('#id-input').value;

    fetch('http://localhost:5000/people/' + id)
    .then(response => response.json())
    .then(data => loadHTMLTable(data));
}

function loadHTMLTable(data) {
    const table = document.querySelector('table tbody');
    console.log('test');
    let tableHtml = "";
    // let i = 1;

    data.forEach(function ({ no, name, yob, sex, school, major }) {
        tableHtml += "<tr>";
        tableHtml += "<td></td>";
        tableHtml += `<td>${no}</td>`;
        tableHtml += `<td>${name}</td>`;
        tableHtml += `<td>${yob}</td>`;
        tableHtml += `<td>${sex}</td>`;
        tableHtml += `<td>${school}</td>`;
        tableHtml += `<td>${major}</td>`;
        tableHtml += "</tr>";
    });

    table.innerHTML = tableHtml;
}