import React from "react";

export default function TravelEntry(props) {
  return(
    <div className="travel-entry">
      <hr className="divider" />
      <div className="travel-name">
        <span className="label"><strong>Task:</strong></span> {props.author}
      </div>
      <div className="travel-location">
        <span className="label"><strong>Place:</strong></span> {props.place}
      </div>
      <div className="travel-lat">
        <span className="label"><strong>Time:</strong></span> {props.lat}
      </div>
      <div className="travel-link">
        <span className="label"><strong>Link:</strong></span> {props.link}
      </div>
    </div>
  )
}