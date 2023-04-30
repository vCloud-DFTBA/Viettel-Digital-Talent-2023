const init = async () => {
  let res = await fetch("/api/attendees", {
    method: "GET",
  })
    .then((response) => {
      if (response.status != 200) {
        return { err: "Error" };
      }
      return response.json();
    })
    .catch((err) => console.log(err));

  if (!res.err) {
    res = eval(res);
    res.sort((a, b) => (a.no < b.no ? -1 : 1));
    res.forEach((element) => {
      let trElement = document.createElement("tr");
      trElement.innerHTML = `<td>${element.no}</td><td>${element.fullName}</td><td>${element.doB}</td><td>${element.gender}</td><td>${element.school}</td><td>${element.major}</td>`;
      document.querySelector(".info-table").appendChild(trElement);
    });
  } else {
    alert("Server get an error");
  }
};

init();