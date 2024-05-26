import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const foto = uploadPhoto();
  const user = createUser();

  Promise.all([foto, user])
    .then((result) => {
      console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
