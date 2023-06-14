import './App.css';
import AttendeeList from './components/AttendeeList'
const App = () => {
  return (
    <div className="container-xl">
      <img src="https://tuyendung.viettel.vn/share/portalHome/images/logo.svg" alt="logo"></img>
	    <div className="table-responsive">
		    <div className="table-wrapper">
            <AttendeeList/>
        </div>
      </div>
    </div>
  );
}

export default App;
