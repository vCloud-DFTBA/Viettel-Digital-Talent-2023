function createTableCell(text) {
    var cell = document.createElement('td');
    cell.textContent = text;
    cell.classList.add('centered-cell');
    return cell;
}

function createButton(className, text, clickHandler) {
    var button = document.createElement('button');
    button.classList.add('button');
    button.classList.add(className);
    button.style.marginRight = '4px';
    button.style.marginBottom = '4px';
    button.textContent = text;
    button.onclick = clickHandler;
    return button;
}

function getStudents(){
fetch('api/students')
    .then(response => response.json())
    .then(data => {
        var studentTable = document.getElementById('studentTable');
        var tbody = studentTable.getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';

        data.forEach(student => {
            var row = document.createElement('tr');

            row.appendChild(createTableCell(student.stt));
            row.appendChild(createTableCell(student.name));
            row.appendChild(createTableCell(student.username));
            row.appendChild(createTableCell(student.birth_year));
            row.appendChild(createTableCell(student.gender));
            row.appendChild(createTableCell(student.university));
            row.appendChild(createTableCell(student.major));

            var actionsCell = document.createElement('td');
            actionsCell.classList.add('centered-cell');
            actionsCell.appendChild(createButton('view-button', 'View', () => viewStudent(student._id)));
            actionsCell.appendChild(createButton('edit-button', 'Edit', () => editStudent(student._id)));
            actionsCell.appendChild(createButton('delete-button', 'Delete', () => deleteStudent(student._id)));
            row.appendChild(actionsCell);
            tbody.appendChild(row);
        });
    });
}

function viewStudent(studentId) {
    window.location.href = '/view?student_id=' + studentId;
}

function editStudent(studentId) {
    var confirmed = confirm('Are you sure you want to edit this student?');
    if (confirmed) {
        window.location.href = '/edit?student_id=' + studentId;
    }
}

function deleteStudent(studentId) {
    var confirmed = confirm('Are you sure you want to delete this student?');
    if (confirmed) {
        fetch('api/students/' + studentId, {
            method: 'DELETE'
        })
            .then(response => {
                getStudents();
            });
    }
    
}
getStudents()