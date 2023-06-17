import { useState, useEffect } from "react";
import TravelEntry from "./components/TravelEntry";
import config from "./config.json";
import React from 'react';
import {
  MDBContainer,
  MDBRow, 
  MDBInput
} from 'mdb-react-ui-kit';

export default function App() {

  let [entries, setEntries] = useState([]);
  let [author, setAuthor] = useState(""); 
  let [place, setPlace] = useState(""); 
  let [lat, setLat] = useState(""); 
  let [link, setLink] = useState(""); 

  const fetchEntries = async () => {
    let locationEntries = await fetch(`${config.BASE_URL}/entries`).then(resp => resp.json());
    setEntries(locationEntries);
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  const handleSubmitBtn = async () => {
    let result = await fetch(`${config.BASE_URL}/entry`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ author, place, lat, link })
    }).then(resp => resp.json());
    fetchEntries();
    handleClearBtn();
    console.log(result);
  }

  const handleClearBtn = () => {
    setAuthor("");
    setPlace("");
    setLat("");
    setLink("")
  }

  const resetForm = async () => {
    let reset = await fetch(`${config.BASE_URL}/clear`).then(resp => resp.json());
    fetchEntries();
    setEntries(locationEntries);
  }

  return (
    <header>
      <div
        className='p-5 text-center bg-image'
        style={{ backgroundImage: "url('https://mdbootstrap.com/img/new/slides/041.webp')", height: 400 }}
      >
        <div className='mask' style={{ backgroundColor: 'rgba(0, 0, 0, 0.6)' }}>
          <div className='d-flex justify-content-center align-items-center h-100'>
            <div className='text-white'>
              <h1 className='mb-3'> Daily Planner </h1>
              <h4 className='mb-3'>Plan your tasks!</h4>
              
              <MDBInput label='Task:' id='formTextExample1' contrast type='text' aria-describedby='textExample1' value={author} onChange={e => setAuthor(e.target.value)} />
      <div id='textExample1' className='form-text'></div>

      <MDBInput label='Place:' id='formTextExample1' contrast type='text' aria-describedby='textExample1' value={place} onChange={e => setPlace(e.target.value)} />
      <div id='textExample1' className='form-text'></div>

      <MDBInput label='Time:' id='formTextExample1' contrast type='text' aria-describedby='textExample1' value={lat} onChange={e => setLat(e.target.value)} />
      <div id='textExample1' className='form-text'></div>

      <MDBInput label='Link Online' id='formTextExample1' contrast type='text' aria-describedby='textExample1' value={link} onChange={e => setLink(e.target.value)} />
      <div id='textExample1' className='form-text' ></div>
              <br></br>
              <a className='btn btn-outline-light btn-lg' onClick={handleSubmitBtn} role='button'>
                Submit
              </a>
              <a className='btn btn-outline-light btn-lg' onClick={handleClearBtn} role='button'>
                Clear Form
              </a>
              <a className='btn btn-outline-light btn-lg' onClick={resetForm} role='button'>
                Clear Entries
              </a>
            </div>
          </div>
          
        </div>
      </div>
      <MDBContainer>
      <MDBRow>
      <div className="mb-3 p-2">
    {entries.map(entry => <TravelEntry {...entry} />)}
</div>
</MDBRow>
</MDBContainer>
    </header>
  );
}