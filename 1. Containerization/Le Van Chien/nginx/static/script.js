const searchBtn = document.querySelector('#search-btn');

searchBtn.onclick = function() {
    const id = document.querySelector('#id-input').value;
    const username = document.querySelector('#username-input').value;

    if (username === "") {
        fetch('http://localhost:8080/people/' + id)
        .then(response => response.json())
        .then(data => loadHTMLTable(data));
    }
    else {
        fetch('http://localhost:8080/people/' + username)
        .then(response => response.json())
        .then(data => loadHTMLTable(data));
    }
}


function sendDeleteRequest(username, btn) {
    fetch('http://localhost:8080/people/delete/' + username, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
            row = btn.parentNode.parentNode;
            row.parentNode.removeChild(row);
        })
        .catch(error => {
        console.error(error);
        // Handle errors
        });
}
  
// Attach event listeners to the delete buttons
document.querySelector('table tbody').addEventListener('click', function(event) {
    if (event.target.className === "delete-row-btn") {
        sendDeleteRequest(event.target.dataset.user, event.target);
    }
    if (event.target.className === "cancel-btn") {
        row = event.target.parentNode.parentNode;
        row.parentNode.removeChild(row);
    }
    if (event.target.className === "submit-btn") {
        addNewAttendee(event.target.parentNode.parentNode)
    }

    if (event.target.className === 'edit-row-btn') {
        getNewData(event.target.parentNode.parentNode, event.target.dataset.user)
    }

    if (event.target.className === 'change-btn') {
        change(event.target.parentNode.parentNode, event.target.dataset.user);
        event.target.parentNode.innerHTML = "<td></td>";
    }

});


// ADD 

addBtn = document.querySelector('#add-btn');

addBtn.onclick = function() {
    const table = document.querySelector('table tbody');
    let tableHtml = "";
    tableHtml += "<tr>";
    tableHtml += `<td><button class="cancel-btn">Cancel</button></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-id"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-name"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-username"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-yob"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-sex"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-school"></td>`;
    tableHtml += `<td><input type="text" style="width:100%;" id="new-major"></td>`;
    tableHtml += `<td><button class="submit-btn">Add</button></td>`;
    tableHtml += "</tr>";

    table.innerHTML += tableHtml;
}


function addNewAttendee(row) {
    var id = row.querySelector('#new-id').value;
    const newAttendee = {
        id: row.querySelector('#new-id').value,
        name: row.querySelector('#new-name').value,
        username: row.querySelector('#new-username').value,
        yob: row.querySelector('#new-yob').value,
        sex: row.querySelector('#new-sex').value,
        school: row.querySelector('#new-school').value,
        major: row.querySelector('#new-major').value
    };


    fetch('http://localhost:8080/people/create/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newAttendee),
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
            row.parentNode.removeChild(row);
        })
}

// update ////////////

function getNewData(row, username) {
    const cells = row.querySelectorAll('td'); // Get all <td> elements within the row
    cells.forEach((cell, index) => {
        const value = cell.textContent;
        if (index == 0) {
            cell.innerHTML = `<td><button class="change-btn" data-user=${username}>Change</td>`;
        }
        else if (index == 3 || index > 7){
            cell.innerHTML = cell.innerHTML;
        }
        else {
            cell.innerHTML = `<input type="text" value="${value}" />`;
        }
    });
  }
  



function change(row, username) {
    const inputs = row.querySelectorAll('input'); // Get all <input> elements within the row

    inputs.forEach(input => {
      const value = input.value;
      input.parentNode.innerHTML = value;
    });

    updateData = {
        id: inputs[0].value,
        name: inputs[1].value,
        yob: inputs[2].value,
        sex: inputs[3].value,
        school: inputs[4].value,
        major: inputs[5].value
    }

    fetch('http://localhost:8080/people/update/' + username, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updateData)
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
        })
}



////////////////////


function loadHTMLTable(data) {
    const table = document.querySelector('table tbody');
    let tableHtml = "";
    // let i = 1;

    data.forEach(function ({ id, name, username, yob, sex, school, major }) {
        tableHtml += "<tr>";
        tableHtml += "<td></td>";
        tableHtml += `<td>${id}</td>`;
        tableHtml += `<td>${name}</td>`;
        tableHtml += `<td>${username}</td>`;
        tableHtml += `<td>${yob}</td>`;
        tableHtml += `<td>${sex}</td>`;
        tableHtml += `<td>${school}</td>`;
        tableHtml += `<td>${major}</td>`;
        tableHtml += `<td><button class="delete-row-btn" data-user=${username}>Delete</td>`;
        tableHtml += `<td><button class="edit-row-btn" data-user=${username}>Edit</td>`;
        tableHtml += "</tr>";
    });

    table.innerHTML = tableHtml;
}