<template>
  <div>
    <h2 class="display-2 my-4 welcome">Welcome</h2>
    <div class="customer-information my-2">
      <b-row>
        <b-col>
          <h2 class="h5 user-information-question">
            <strong>Your company name is:</strong>
          </h2>
        </b-col>
        <b-col>
          <h2 class="h5 user-information-answer">{{ company }}</h2>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <h2 class="h5 user-information-question">
            <strong>Your location is:</strong>
          </h2>
        </b-col>
        <b-col>
          <h2 class="h5 user-information-answer">{{ location }}</h2>
        </b-col>
      </b-row>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      company: "Company",
      location: "123 Fake Street, Australia"
    };
  }
};
</script>
<style scoped>
.customer-information {
  padding: 2%;
  border-style: solid;
  border-color: #a0fff5;
  border-radius: 10px;
}

.user-information-answer {
  color: white;
  margin: 5px;
  text-align: left;
}

.user-information-question {
  color: white;
  margin: 5px;
  text-align: right;
}

.welcome {
  color: white;
  text-align: center;
  margin: 15px;
  margin-top: 3%;
}
</style>
