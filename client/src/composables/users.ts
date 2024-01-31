import { Ref, ref } from "vue";
import { axiosInstance } from "../axios";

export default function useUsers() {
  const user: Ref<User> = ref<User>();
  const users: Ref<User[]> = ref<User[]>();

  async function getUserById(id: number) {
    const response = await axiosInstance.get(`/users/${id}`);
    user.value = response.data.user;
  }

  async function getUsers() {
    const response = await axiosInstance.get("/users");
    users.value = response.data.users;
  }

  async function createUser(name: string, email: string, address: string) {
    const body = {
      name: name,
      email: email,
      address: address,
    };
    await axiosInstance.post("/users", body);
  }

  return {
    user,
    users,
    getUsers,
    createUser,
    getUserById,
  };
}
