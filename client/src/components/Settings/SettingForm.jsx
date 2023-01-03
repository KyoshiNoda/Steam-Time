import React,{useState} from 'react';
import PasswordModal from './Modal/PasswordModal';
import SaveModal from './Modal/SaveModal';
function SettingForm() {
  const [firstName,setFirstName] = useState();
  const [lastName,setLastName] = useState();
  const [email,setEmail] = useState();
  const [apiKey,setApiKey] = useState();
  const [username,setUsername] = useState("Dlyan");
  const [saveModal,setSaveModal] = useState(false);

  const formHandler = (event) =>{
    event.preventDefault();
  }
  const saveModalHandler = () =>{
    setSaveModal(true);
    setInterval(()=>{
      setSaveModal(false);
    },3000)
  };

  const firstNameHandler = (event) =>{
    setFirstName(event.target.value);
    console.log(firstName);
  };

  const lastNameHandler = (event) =>{
    setLastName(event.target.value);
    console.log(lastName);
  };

  const emailHandler = (event) =>{
    setEmail(event.target.value);
    console.log(email);
  };

  const apiKeyHandler  = (event) =>{
    setApiKey(event.target.value);
    console.log(apiKey);
  }
  const userNameHandler = (event) =>{
    setUsername(event.target.value);
    console.log(username);
  }


  return (
    <form onSubmit = {formHandler}>
      <div className="flex m-10">
        <div className="flex-1 first:mr-10">          
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">User Name</span>
            </label>
            <input
              onChange={userNameHandler}
              type="text"
              placeholder="epicman2313"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">First Name</span>
            </label>
            <input
              onChange={firstNameHandler}
              type="text"
              placeholder="John"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">Last Name</span>
            </label>
            <input
              onChange={lastNameHandler}
              type="text"
              placeholder="Doe"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
        </div>

        <div className="mr-10">
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">Steam URL</span>
            </label>
            <input
              onChange = {emailHandler}
              type="text"
              placeholder="https://steamcommunity.com/id/Dilian1"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">API Key</span>
            </label>
            <input
              onChange={apiKeyHandler}
              type="text"
              placeholder="JH2H32K3214H1213"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
          <div className="form-control w-full max-w-xs">
            <label className="label">
              <span className="label-text lg:text-xl">Email</span>
            </label>
            <input
              onChange={apiKeyHandler}
              type="text"
              placeholder="JohnDoe@gmail.com"
              className="input input-bordered w-full max-w-xs"
            />
          </div>
        </div>
      </div>
      <div className="flex justify-center gap-5">
        <button className="btn btn-outline btn-success" onClick ={saveModalHandler}>Save Changes</button>
        <PasswordModal/>
        {saveModal === true ? <SaveModal/> : <></>}
      </div>
    </form>
  );
}

export default SettingForm;
