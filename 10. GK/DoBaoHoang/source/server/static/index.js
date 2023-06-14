let tableBody = document.getElementById("attendees");
let tableHead = document.getElementById("headTable");
let titlePage = document.getElementById("pageTitle");
const baseURL = '/api';

// Initiate Table
const cols = ["Họ và tên", "Năm sinh", "Giới tính", "Đại học", "Chuyên ngành", "Action"];
cols.forEach(col_name => {
    let col = document.createElement("th");
    col.innerHTML = `${col_name}`;
    col.setAttribute("scope", "col");
    tableHead.appendChild(col);
});

function appendCellData(parent, val) {
    let cell = document.createElement("td");
    cell.innerHTML = `${val}`;
    parent.appendChild(cell);
};

fetch(baseURL + '/profiles')
    .then(resp => resp.json())
    .then(data => {
        data.attendees.forEach(attendee => {
            titlePage.textContent = `IP: ${data.ip}`;
            let row = document.createElement("tr");
            appendCellData(row, attendee.name);
            appendCellData(row, attendee.birth_year);
            appendCellData(row, attendee.gender);
            appendCellData(row, attendee.university);
            appendCellData(row, attendee.major);
            appendCellAction(row, attendee);
            tableBody.appendChild(row)
        });
    })
    .catch(err => {
        console.log(err);
    })

/* <li><a href="#" data-tip="edit" data-bs-toggle="modal" data-bs-target="#modalUpdate"><i class="fa fa-edit"></i></a></li> */                                 

function appendCellAction(parent, attendee) {
    let cell = document.createElement("td");
    let list = document.createElement("ul");
    list.className = "action-list";
    
    let itemEdit = document.createElement("li");
    let linkEdit = document.createElement("a");
    linkEdit.href = "#";
    linkEdit.dataset.id = attendee._id;
    linkEdit.dataset.name = attendee.name;
    linkEdit.dataset.birth_year = attendee.birth_year;
    linkEdit.dataset.gender = attendee.gender;
    linkEdit.dataset.university = attendee.university;
    linkEdit.dataset.major = attendee.major;
    linkEdit.dataset.tip = "edit";
    linkEdit.dataset.bsToggle = "modal";
    linkEdit.dataset.bsTarget = "#modalUpdate";
    let iconEdit = document.createElement("i");
    iconEdit.className = "fa fa-edit";
    linkEdit.appendChild(iconEdit)
    itemEdit.appendChild(linkEdit);
    list.appendChild(itemEdit);
    
    let itemDelete = document.createElement("li");
    let linkDelete = document.createElement("a");
    linkDelete.href = "#";
    linkDelete.dataset.id = attendee._id;
    linkDelete.dataset.tip = "delete";
    linkDelete.dataset.bsToggle = "modal";
    linkDelete.dataset.bsTarget = "#modalDelete";
    let iconDelete = document.createElement("i");
    iconDelete.className = "fa fa-trash";
    linkDelete.appendChild(iconDelete)
    itemDelete.appendChild(linkDelete);
    list.appendChild(itemDelete);

    cell.appendChild(list);
    parent.appendChild(cell);
}

// Handle Forms

function refreshPage() {
    document.location.href = '/';
}

// Handle form Create
const formCreate = document.getElementById('formCreate');
const btnCreate = document.getElementById('btnCreate');
btnCreate.addEventListener('click', () => {
    const formData = new FormData(formCreate);

    fetch(baseURL + '/profile/create', {
        method: 'POST',
        body: new URLSearchParams(formData),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(resp => {
        console.log(resp);
        refreshPage();
    })
    .catch(error => {
        console.log(error);
    })
})

// Handle form Update
const formUpdate = document.getElementById('formUpdate');
const btnUpdate = document.getElementById('btnUpdate');
const modalUpdate = document.getElementById('modalUpdate');
btnUpdate.addEventListener('click', () => {
    const id = btnUpdate.dataset.id;
    const formData = new FormData(formUpdate);
    
    fetch(baseURL + `/profile/${id}`, {
        method: 'PUT',
        body: new URLSearchParams(formData),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(resp => {
        console.log(resp);
        refreshPage();
    })
    .catch(error => {
        console.log(error);
    })
})

modalUpdate.addEventListener('show.bs.modal', event =>{
    const btn = event.relatedTarget;
    const id = btn.getAttribute('data-id');
    btnUpdate.dataset.id = id;
    document.getElementById('modalUpdateTitle').textContent = "Update Attendee: " + btn.getAttribute('data-name');
    document.getElementById('update_birth_year').value = btn.getAttribute('data-birth_year');
    document.getElementById('update_gender').value = btn.getAttribute('data-gender');
    document.getElementById('update_university').value = btn.getAttribute('data-university');
    document.getElementById('update_major').value = btn.getAttribute('data-major');
})

// Handle form Delete
const formDelete = document.getElementById('formDelete');
const btnDelete = document.getElementById('btnDelete');
const modalDelete = document.getElementById('modalDelete');
btnDelete.addEventListener('click', () => {
    const id = btnDelete.dataset.id;
    
    fetch(baseURL + `/profile/${id}`, {
        method: 'DELETE'
    })
    .then(resp => {
        console.log(resp);
        refreshPage();
    })
    .catch(error => {
        console.log(error);
    })
})

modalDelete.addEventListener('show.bs.modal', event =>{
    const btn = event.relatedTarget;
    const id = btn.getAttribute('data-id');
    btnDelete.dataset.id = id;
})

