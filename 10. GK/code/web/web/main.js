// api url
const apiURL = "http://192.168.238.134:8000/Attendees/";

// Defining async function
async function getapi(url) {
  // Storing response
  const response = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  });

  // Storing data in form of JSON
  var data = await response.json();
  console.log(data);
  if (response) {
    hideloader();
  }
  show(data);
}
// Calling that async function
getapi(apiURL);

// Function to hide the loader
function hideloader() {
  document.getElementById("loading").style.display = "none";
}
// Function to define innerHTML for HTML table
function show(data) {
  let tab = `<thead>
		<tr>
			<th scope="col">STT</th>
			<th scope="col">Họ và tên</th>
			<th scope="col">Username</th>
			<th scope="col">Năm sinh</th>
			<th scope="col">Giới tính</th>
			<th scope="col">Trường đại học</th>
			<th scope="col">Chuyên ngành</th>
			<th scope="col">Hành động</th>
		</tr>
	</thead>
	<tbody>`;

  // Loop to access all rows
  for (let r of data) {
    tab += `
			<tr class="attendee-item-${r.id}">
                <th scope="row">${r.id}</th>
                <td>${r.full_name}</td>
                <td>${r.username}</td>
                <td>${r.DoB}</td>
                <td>${r.gender}</td>
                <td>${r.university_name}</td>
                <td>${r.major}</td>
                <td>
                    <button id="btn_edit_attendee" onclick="handleEditAttendee(${r.id})" >
                        <i class="fas fa-user-edit" ></i>
                        Sửa
                    </button>
                    
                    <button>
                        <i class="fas fa-info"></i>
                        Xem chi tiết
                    </button>
                    <button id="btn_delete_attendee" onclick="handleDeleteAttendee(${r.id})">
                        <i class="fas fa-user-times" ></i>
                        Xóa
                    </button>
                </td>
            </tr>`;
  }
  tab += `</tbody>`;
  // console.log(tab);
  // Setting innerHTML as tab variable
  document.getElementById("attendees").innerHTML = tab;
}

let delete_modal = document.getElementsByClassName("delete_modal");
let accept_button = document.getElementById("btn_accept_button");
var cancel_button = document.getElementById("btn_cancel_button");
let delete_attendee = document.querySelector("#btn_delete_attendee");
let btn_edit_attendee = document.getElementById("btn_edit_attendee");

function handleClickDeleteModal() {
  delete_modal[0].classList.toggle("hidden");
}

function handleClickEditModal() {
  edit_modal[0].classList.toggle("hidden");
}

function handleDeleteAttendee(item_id) {
  handleClickDeleteModal();
  accept_button.onclick = () => {
    fetch(apiURL + item_id, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    handleClickDeleteModal();
    var itemdeleted = document.querySelector(".attendee-item-" + item_id);
    if (itemdeleted) {
      itemdeleted.remove();
    }
    return;
  };
  cancel_button.onclick = () => {
    handleClickDeleteModal();
    return;
  };
}

function handleEditAttendee(item_id) {
  return fetch(apiURL + item_id, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      renderEditModal(data);

      showEditModal();

      //   Cancel edit and close modal
      var btn_cancel_edit_infor = document.getElementById(
        "btn_cancel_edit_infor"
      );
      btn_cancel_edit_infor.addEventListener("click", function () {
        closeEditModal();
      });
      var btn_accept_edit_button = document.getElementById(
        "btn_accept_edit_button"
      );
      btn_accept_edit_button.addEventListener("click", function () {
        var inputNameUpdate = document.getElementsByName("inputName")[0].value;
        var inputUsernameUpdate =
          document.getElementsByName("inputUsername")[0].value;
        var inputDoBUpdate =
          document.getElementsByClassName("inputDoB")[0].value;
        var inputUniversityUpdate =
          document.getElementsByName("inputUniversity")[0].value;
        var inputMajorUpdate =
          document.getElementsByName("inputMajor")[0].value;
        var inputGender = document.getElementById("gender");
        var selectedIndex = inputGender.selectedIndex;
        var inputGenderUpdate = inputGender.options[selectedIndex].value;
        console.log(inputNameUpdate);
        dataUpdated = {
          full_name: inputNameUpdate,
          //   username: inputUsernameUpdate,
          //   DoB: inputDoBUpdate,
          //   university_name: inputUniversityUpdate,
          //   major: inputMajorUpdate,
          //   gender: inputGenderUpdate,
        };
        callUpdateAPI(item_id, dataUpdated);
        closeEditModal();
      });
    });
}

function callUpdateAPI(item_id, dataUpdated) {
  fetch(apiURL + item_id, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: dataUpdated,
  });
}

function renderEditModal(data) {
  var modal = document.createElement("div");
  modal.id = "edit_modal";
  modal.className = "edit_modal";
  modal.innerHTML = `
	<div class="edit_container_modal">
		<div class="edit_header_modal">
			Chỉnh sửa thông tin học viên
		</div>
		<div class="edit_content_modal">
			<form method="post">

				<!-- Text input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="form6Example3">Họ và tên</label>
					<input type="text" id="form6Example3" class="form-control" name="inputName" autocomplete="off" />
					
				</div>
				<!-- Text input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="form6Example3">Username</label>
					<input type="text" id="form6Example3" name="inputUsername" class="form-control" value= ${data.username} />
					
				</div>
				<!-- 2 column grid layout with text inputs for the first and last names -->
				<div class="row mb-4">
					<div class="col">
						<div class="form-outline">
							<label class="form-label" for="form6Example1"> Năm sinh</label>
							<input type="text" id="form6Example1" class="form-control inputDoB" value=${data.DoB} />
							
						</div>
					</div>
					<div class="col parent_gender_input">
						<div class="form-outline gender_input">
							<label class="form-label" for="form6Example2">Giới tính:</label>
							<select name="gender" id="gender">
								<option value="Nam">Nam</option>
								<option value="Nữ">Nữ</option>
							  </select>
							
						</div>
					</div>
				</div>
				<!-- Text input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="form6Example4">Trường đại học</label>
					<input type="text" id="form6Example4" class="form-control" name="inputUniversity" />
					
				</div>
				<!-- Text input -->
				<div class="form-outline mb-4">
					<label class="form-label" for="form6Example4">Chuyên ngành</label>
					<input type="text" id="form6Example4" class="form-control" name="inputMajor" />
					
				</div>
				
			</form>
		</div>
		<div class="edit_footer_modal">
			<button class="accept_button" id="btn_accept_edit_button">Xác nhận</button>
			<button class="cancel_button" id="btn_cancel_edit_infor">Hủy thay đổi</button>
		</div>
	</div>`;
  document.body.appendChild(modal);
  document
    .getElementsByName("inputName")[0]
    .setAttribute("value", data.full_name);
  document
    .getElementsByName("inputUniversity")[0]
    .setAttribute("value", data.university_name);
  document.getElementsByName("inputMajor")[0].setAttribute("value", data.major);
  var valueGender = data.gender;
  console.log(valueGender);
  var genderSelected = document.getElementById("gender");
  for (var i = 0; i < 2; i++) {
    if (genderSelected.options[i].value == valueGender) {
      genderSelected.options[i].selected = true;
      break;
    }
  }
}

function showEditModal() {
  var modal = document.getElementById("edit_modal");
  modal.style.display = "flex";
}

function closeEditModal() {
  var modal = document.getElementById("edit_modal");
  modal.parentNode.removeChild(modal);
}
// handleEditAttendee(item_id).then(() => {

// })

// full_name = "abc";

// let edit_modal = document.getElementsByClassName("edit_modal");
// let btn_cancel_edit_infor = document.getElementById("btn_cancel_edit_infor");
// // function handleClickEditModal() {
// // 	edit_modal[0].classList.toggle("hidden");
// // }
// btn_cancel_edit_infor.addEventListener('click', () => {
// 	// handleClickEditModal();
// 	edit_modal[0].classList.toggle("hidden");
// })
