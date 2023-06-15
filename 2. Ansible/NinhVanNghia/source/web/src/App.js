import {attendeeQuery} from "./api/attendeeQuery";


function App() {
    const {data, status} = attendeeQuery.useList({query: {page:0, limit: 100}})

    return (
        <div className="App">
            VDT APP
            <div className="container">
                <div className="row">
                    <div className="col-3">Ho Va Ten</div>
                    <div className="col-2">Nam sinh</div>
                    <div className="col-7">Truong</div>
                </div>
                {status === "success" && 
                data.attendees.map(item => <Row {...item}/>)}
            </div>
        </div>
  );
}

export default App;


function Row({fullname, birthYear, university}) {
    return (
        <div className="row">
            <div className="col-3">{fullname}</div>
            <div className="col-2">{birthYear}</div>
            <div className="col-7">{university}</div>
        </div>
    )
}
