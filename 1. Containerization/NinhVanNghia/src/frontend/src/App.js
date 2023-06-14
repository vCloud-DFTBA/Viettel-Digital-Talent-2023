import axios from 'axios';
import {useState, useEffect} from 'react';

function App() {
  const [attendees, setAttendees] = useState('Loading');
  useEffect(() => {
    (async () => {
      const response = await axios.get(`/api/v1/attendee`)
      setAttendees(response.data)
    })()
  }, []);
  return (
    <div className="App">
      <h1>SMS APP</h1>
      {attendees}
    </div>
  );
}

export default App;
