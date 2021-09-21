import React, { useState } from 'react';
import mockdata from './api-mock.json';

const App = () => {
  const [matchList, setMatchList] = useState(mockdata._default)
  return (
    <div>
      {
        Object.keys(matchList).map((match, index) => {
          var url = "https://matches.telugumatrimony.com/search-by-id/viewprofile/" + matchList[match].MATRIID;
          return (
            <div className="image-grid" key={index}>
              <div className="one" key={index} >
                {/* {console.log(index)} */}
                <img key={index} src={matchList[match].THUMBNAME} alt={matchList[match].NAME}></img>
              </div>
              <div className="two">
                ID: {matchList[match].MATRIID}<br/>
                Name: {matchList[match].NAME}<br/>
                Age: {matchList[match].MEMAGE}<br/>
                Height: {matchList[match].HEIGHT}<br/>
                Star: {matchList[match].STAR}<br/>
                Country: {matchList[match].COUNTRY}<br/>
                State: {matchList[match].STATE}<br/>                
                <a href={url} target="_blank">Open</a>
              </div>
            </div>
          )
        })
      }
    </div>
  )
}

export default App
