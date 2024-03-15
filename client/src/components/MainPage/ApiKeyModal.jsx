import { useRef, useState } from 'react';
import { Button, Modal } from 'react-daisyui';
import { useAppDispatch, useAppSelector } from '../../redux/store';
import { closeAPIKeyModal } from '../../redux/feats/globalSlice/globalSlice';
import axios from 'axios';
import { updateUserDetails } from '../../redux/feats/auth/authSlice';

const ApiKeyModal = () => {
  const apiKeyRef = useRef(null);
  const isOpen = useAppSelector((state) => state.global.isApiKeyModalOpen);
  const steamID = useAppSelector((state) => state.auth.user.steam_id);
  const dispatch = useAppDispatch();
  const [errorMessage, setErrorMessage] = useState('');
  const [isError, setIsError] = useState(false);

  const updateAPIKeyHandler = () => {
    axios
      .post('http://localhost:8000/api/steam_auth/new-user', {
        api_key: apiKeyRef.current.value,
        steam_id: steamID,
      })
      .then((res) => {
        dispatch(updateUserDetails(res.data.updatedUser))
        dispatch(closeAPIKeyModal());
      })
      .catch((error) => {
        setIsError(true);
        setErrorMessage(error.response.data.error);
      });
  };

  return (
    <Modal open={isOpen} className="flex flex-col gap-2">
      <Modal.Header className="text-white text-center text-lg font-bold">
        Welcome to SteamTime!
      </Modal.Header>
      <Modal.Body>
        <h1 className="text-center">Please enter API KEY to get started!</h1>
        <div className="flex justify-center gap-2">
          <label className="flex text-md text-white items-center">
            API KEY:
          </label>
          <div className='inline-block'>
            <input
              type="password"
              ref={apiKeyRef}
              className={`mt-2 p-2 border rounded-md focus:outline-none focus:border-blue-500 w-full ${
                isError ? 'border-rose-500' : 'border-gray-300'
              }`}
            />
            {isError && (
              <div className="text-xs text-red-500">
                {errorMessage}
              </div>
            )}
          </div>
        </div>
        <div className="flex flex-col items-center">
          <h1>Not sure where it's located?</h1>
          <a
            href="https://steamcommunity.com/dev"
            className="cursor-pointer underline"
          >
            Click Here
          </a>
        </div>
      </Modal.Body>
      <Modal.Actions className="flex justify-center gap-4">
        <Button
          onClick={updateAPIKeyHandler}
          className=" bg-blue-500 text-white hover:bg-blue-600"
        >
          Save
        </Button>
        <Button
          onClick={() => dispatch(closeAPIKeyModal())}
          className="bg-gray-300 text-gray-800 hover:bg-gray-400"
        >
          Close
        </Button>
      </Modal.Actions>
    </Modal>
  );
};

export default ApiKeyModal;
