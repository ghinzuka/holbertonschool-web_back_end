import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const resultPhoto = await uploadPhoto();
    const resultUser = await createUser();
    return {
      photo: resultPhoto,
      user: resultUser,
    };
  } catch (error) {
    return {
      photo: null,
      user: null,
    };
  }
}
