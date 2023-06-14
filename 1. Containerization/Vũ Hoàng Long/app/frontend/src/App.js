import { useState, useLayoutEffect } from 'react';

function App() {

  const [attendees, setAttendees] = useState([])

  const url = `http://localhost:5000/get_all`

  useLayoutEffect(() => {
    ;
    (function getAttendees(){
      fetch(url,  {
        method: 'GET',
        headers: {
          Accept: 'application/json',
        }}) // fetch data từ api ve
      .then(response => response.json())
      .then(data =>{ 
        setAttendees(data)
    })
    })()
  }, [])


  return (
    <div className="App">
      <h3>
      Danh sách sinh viên thực tập VDT-2023
      </h3>
      
      <div>
              <table>
                <tr>
                  <th>STT</th>
                  <th>Họ và tên</th>
                  <th>Năm sinh</th>
                  <th>Giới tính</th>
                  <th>Trường</th>
                  <th>Chuyên ngành</th>
                </tr>
                {
                  attendees.map((attendee) => (
                    <tr key={attendee.stt}>
                      <td >{attendee.stt}</td>
                      <td >{attendee.ten}</td>
                      <td >{attendee.nam}</td>
                      <td >{attendee.gt}</td>
                      <td >{attendee.truong}</td>
                      <td >{attendee.nganh}</td>
                    </tr>
                    ))
                }
                </table>
      </div>
    </div>
  );
}

export default App;