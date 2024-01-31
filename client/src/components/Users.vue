<template>
  <div class="bg-body-tertiary rounded-3 mt-5 p-3">
    <form @submit.prevent="onSubmit">
      <div class="mb-3">
        <label for="nameInput" class="form-label">Name</label>
        <input
          type="text"
          v-model="form.name"
          id="nameInput"
          class="form-control"
        />
      </div>

      <div class="mb-3">
        <label for="emailInput" class="form-label">Email address</label>
        <input
          type="email"
          v-model="form.email"
          id="emailInput"
          class="form-control"
        />
      </div>
      <div class="mb-3">
        <label for="addressInput" class="form-label">Address</label>
        <textarea
          v-model="form.address"
          id="addressInput"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-success">Submit</button>
    </form>
  </div>

  <table class="table mt-5">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Email</th>
        <th scope="col">Address</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <th scope="row">{{ user.id }}</th>
        <td>{{ user.name }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.address }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { onMounted } from "vue";
import useUsers from "../composables/users";

export default {
  name: "Users",
  setup() {
    const { users, getUsers, createUser } = useUsers();
    const form = {
      name: "",
      email: "",
      address: "",
    };

    async function onSubmit() {
      await createUser(form.name, form.email, form.address).then(getUsers);
    }

    onMounted(getUsers);
    return {
      users,
      form,
      onSubmit,
    };
  },
};
</script>
