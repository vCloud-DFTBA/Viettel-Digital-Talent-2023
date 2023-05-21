import AttendeeRow from "./components/AttendeeRow";
import CreateButton from "./components/CreateButton";

import {attendeeQuery} from "api/attendeeQuery";


function Home() {
    const {data, status} = attendeeQuery.useList({query: {page:0, limit: 100}})
    return (
        <div className="container">
            <div className="d-flex flex-row mb-1">
                <CreateButton className="ms-auto"/>
            </div>
            <div className="row border-bottom">
                <div className="col-3">Họ Và Tên</div>
                <div className="col-2">Năm sinh</div>
                <div className="col-5">Trườnng</div>
                <div className="col-2">thao tác</div>
            </div>
            {status === "success" && 
            data.attendees.map(item => <AttendeeRow {...item} key={item.attendeeId}/>)}
        </div>
    )
}


export default Home
