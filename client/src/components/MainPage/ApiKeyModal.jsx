import { useRef } from 'react';
import { Button, Modal } from 'react-daisyui';
import { useAppDispatch, useAppSelector } from '../../redux/store';
import { closeAPIKeyModal } from '../../redux/feats/globalSlice/globalSlice';

const ApiKeyModal = () => {
  const apiKeyRef = useRef(null);
  const isOpen = useAppSelector((state) => state.global.isApiKeyModalOpen);
  const dispatch = useAppDispatch();

  const updateAPIKeyHandler = () => {
    console.log('TEST FOR NOW');
  };

  return (
    <Modal open={isOpen} className="flex flex-col gap-10">
      <Modal.Header className="text-white text-center text-lg font-bold">
        Welcome to SteamTime!
      </Modal.Header>
      <Modal.Body>
        <div className="flex  justify-center gap-2">
          <label className="flex text-md text-white items-center">
            API KEY:
          </label>
          <input
            type="text"
            ref={apiKeyRef}
            className="mt-2 p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 w-1/2"
          />
        </div>
      </Modal.Body>
      <Modal.Actions className="flex justify-center">
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
