import React, { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import Loader from "./loader";
import logoLGM from "./logoLGM.png";

const App = () => {
  const [userCardData, setUserCardData] = useState([]);
  const [visibility, setVisibility] = useState(false);
  const [loading, setLoading] = useState(false);

  const allData = async () => {
    if (visibility) {
      const response = await axios.get("https://reqres.in/api/users?page=1");
      const delay = 2000;
      await new Promise((resolve) => setTimeout(resolve, delay));
      setUserCardData(response.data.data);
    }
    setLoading(false);
  };

  const display = () => {
    setVisibility(true);
    setLoading(true);
  }
  useEffect(() => {
    if (visibility) {
      allData();
    } // eslint-disable-next-line
  }, [loading]);

  const renderUserCard = (user) => {
    if (loading) {
      return Loader;
    }
    else {
      return (
        <div className="userCard div text-center">
          <img
            src={user.avatar}
            alt=""
            className="round-img"
            style={{ width: "40%" }}
          />
          <h3>User ID : {user.id}</h3>
          <h3>User Name : {user.first_name} {user.last_name}</h3>
          <h3>EMail : {user.email}</h3>
        </div>
      );
    }
  };
  return (
    <div className="App">
      <nav className="navbar" style={{ backgroundColor: "grey" }}>
        <img src={logoLGM} alt="" style={{ height: "110%", width: "30%" }} />
        <button
          className="button"
          style={{ backgroundColor: "black" }}
          onClick={display}
        >
          Get Users
        </button>
      </nav>

      {loading ? <Loader /> : null}
      <div className="userCardContainer" style={userStyle}>
        {loading ? null : userCardData.map(renderUserCard)}
      </div>
    </div>
  );
};

const userStyle = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit,min(300px))",
  gridGap: "3rem",
  marginBottom: "10%",
};

export default App;
