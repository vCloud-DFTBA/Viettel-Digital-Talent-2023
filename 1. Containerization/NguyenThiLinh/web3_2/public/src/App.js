import React from "react";
import axios from 'axios';
class App extends React.Component {



  constructor(props) {
    super(props);
    this.state =
    {
      users: [],
      id: 0,
      no: 0,
      fullName: '',
      doB: null,
      gender: '',
      school: '',
      major: ''
    }
  }
  componentDidMount() {
    axios.get('http://localhost:5000/')
      .then((res) =>
        this.setState({
          users: res.data,
          id: 0,
          no: 0,
          fullName: '',
          doB: null,
          gender: '',
          school: '',
          major: ''
        })
      )
  }

  fullNamechange = event => {
    this.setState({
      fullName: event.target.value
    })
  }

  nochange = event => {
    this.setState({
      no: event.target.value
    })
  }
  doBchange = event => {
    this.setState({
      doB: event.target.value
    })
  }
  genderchange = event => {
    this.setState({
      gender: event.target.value
    })
  }
  schoolchange = event => {
    this.setState({
      school: event.target.value
    })
  }
  majorchange = event => {
    this.setState({
      major: event.target.value
    })
  }
  submit(event, id) {
    console.log(id)
    event.preventDefault()
    if (id === 0) {
      axios.post('http://localhost:5000', { "fullName": this.state.fullName, "no": this.state.no, "doB": this.state.doB, "gender": this.state.gender, "school": this.state.school, "major": this.state.major })
        .then(() => {
          this.componentDidMount();
        })
    } else {
      axios.put(`http://localhost:5000/${id}`, { "fullName": this.state.fullName, "no": this.state.no, "doB": this.state.doB, "gender": this.state.gender, "school": this.state.school, "major": this.state.major })
        .then(() => {
          this.componentDidMount();
        })
    }
    this.setState({
      id: 0,
      no: 0,
      fullName: '',
      doB: '',
      gender: '',
      school: '',
      major: ''
    });
    alert("Submited!!")
    return undefined;


  }

  delete(id) {
    axios.delete(`http://localhost:5000/${id}`)
      .then(() => {
        this.componentDidMount();
      })
  }

  getone(id) {
    axios.get(`http://localhost:5000/getone/${id}`)
      .then((res) => {
        // console.log(res.data)
        this.setState({
          fullName: res.data.fullName,
          doB: res.data.doB,
          gender: res.data.gender,
          school: res.data.school,
          major: res.data.major,
          id: res.data._ID
        })
      })
  }

  render() {
    // const tableStyle= `table {
    //   counter-reset: rowNumber;
    // }
    
    // table tr {
    //   counter-increment: rowNumber;
    // }
    
    // table tr td:first-child:before {
    //   content: counter(rowNumber);
    // }
    // `
    return (
        <div className="mt-5">

          <h1 className="text-center pt-5"> Attendees' Information </h1>

          <div className="row d-flex justify-content-evenly">
            <div className="col-2 m-5">
              <form onSubmit={(e) => { this.submit(e, this.state.id) }}>
                {/* <div className="form-group mt-2">
                <input id="number" type="number" onChange={(e) => { this.nochange(e) }} className="form-control" placeholder="No." />
              </div> */}
                <h5 className="mt-5 text-center"> Add new or Update Attendee</h5>
                <div className="form-group mt-2">
                  <input required type="text" onChange={(e) => { this.fullNamechange(e) }} className="form-control" placeholder="Full Name" value={this.state.fullName} />
                </div>
                <div className="form-group mt-2">
                  <input type="number" onChange={(e) => { this.doBchange(e) }} className="form-control" placeholder="Year of Birth" value={this.state.doB} />
                </div>
                <div className="form-group mt-2">
                  <input type="text" onChange={(e) => { this.genderchange(e) }} className="form-control" placeholder="Gender" value={this.state.gender} />
                </div>
                <div className="form-group mt-2">
                  <input type="text" onChange={(e) => { this.schoolchange(e) }} className="form-control" placeholder="School" value={this.state.school} />
                </div>
                <div className="form-group mt-2">
                  <input type="text" onChange={(e) => { this.majorchange(e) }} className="form-control" placeholder="Major" value={this.state.major} />
                </div>
                <div className="d-flex align-items-center justify-content-center">
                  <button className="btn btn-primary mt-2 "> Submit </button>
                </div>
              </form>
            </div>


            <div className="col-8 mr-5 my-5">
              <table  className="table table-responsive table-bordered table-striped">
                <thead>
                  <tr>
                    {/* <th> No </th> */}
                    <th> Full Name </th>
                    <th> Year of Birth  </th>
                    <th> Gender </th>
                    <th> School </th>
                    <th> Major </th>
                    <th> Edit </th>
                    <th> Delete </th>
                  </tr>
                </thead>
                <tbody>



                  {this.state.users.map(user =>
                    <tr>
                      {/* <td></td> */}
                      <td>{user.fullName}</td>
                      <td>{user.doB}</td>
                      <td>{user.gender}</td>
                      <td>{user.school}</td>
                      <td>{user.major}</td>
                      <td>
                        <button onClick={(e) => this.getone(user._ID)} className="btn btn-sm btn-primary">
                          <i className="fa-solid fa-pencil"></i>
                        </button>
                      </td>
                      <td>
                        <button onClick={(e) => this.delete(user._ID)} className="btn btn-sm btn-danger">
                          <i className="fa fa-trash"></i>
                        </button>
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
    );
  }
}

export default App;
