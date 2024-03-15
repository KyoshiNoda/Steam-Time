import { useEffect } from 'react';
import { useAppDispatch, useAppSelector } from '../redux/store';
import { updateUserDetails } from '../redux/feats/auth/authSlice';
import ApiKeyModal from '../components/MainPage/ApiKeyModal';
import { openAPIKeyModal } from '../redux/feats/globalSlice/globalSlice';

const MainPage = () => {
  const dispatch = useAppDispatch();

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const message = params.get('message');
    const userString = params.get('user');

    if (message && userString) {
      const parseUser = JSON.parse(userString);
      dispatch(updateUserDetails(parseUser));
      if (!parseUser.api_key) {
        dispatch(openAPIKeyModal());
      }
    }
  }, []);

  const user = useAppSelector((state) => state.auth.user);
  const isApiKeyModalOpen = useAppSelector(
    (state) => state.global.isApiKeyModalOpen
  );

  return (
    <>
      <div className="h-screen w-screen flex justify-center items-center">
        <div className="bg-white rounded-lg p-4 h-1/2 w-1/2 text-black">
          <div>
            <span className="underline ">User ID:</span> {user.user_id}
          </div>
          <div>
            <span className="underline ">Steam ID:</span> {user.steam_id}
          </div>
          <div>
            <span className="underline ">Login Type:</span> {user.login}
          </div>
        </div>
      </div>
      {isApiKeyModalOpen && <ApiKeyModal />}
    </>
  );
};

export default MainPage;
