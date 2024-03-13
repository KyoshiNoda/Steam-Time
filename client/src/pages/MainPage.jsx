import { useEffect } from 'react';
const MainPage = () => {
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const message = params.get('message');
    const userString = params.get('user');

    if (message && userString) {
      const user = JSON.parse(userString);
      console.log(message, user);
    }
  }, []);
  return (
    <div className="h-screen w-screen flex justify-center items-center">
      <div className="bg-white rounded-lg p-4 h-1/2 w-1/2">
        <div>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi
          voluptatem molestiae dolor quod officia dignissimos ullam sapiente
          pariatur cupiditate! Tenetur, vel perspiciatis. Hic quidem quam vero
          placeat consectetur excepturi quas? Dolore similique nihil, nemo
          molestiae nam accusamus unde dolorum excepturi officia omnis,
          perspiciatis voluptatibus, officiis placeat exercitationem doloribus
          totam ex temporibus hic aut vel laboriosam facere culpa! Vel, delectus
          quasi.
        </div>
      </div>
    </div>
  );
};

export default MainPage;
