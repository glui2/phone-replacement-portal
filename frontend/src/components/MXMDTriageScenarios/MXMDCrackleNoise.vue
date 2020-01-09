<template>
  <div style="text-align: center">
    <b-row class="triage-radio-question">
      <b-form-group
        label="While on a phone call, wiggle the curly cord. Does this create any crackling noises?"
      >
        <b-form-radio-group
          id="S12-Q1"
          v-model="hasCracklingNoises"
          :options="options"
          buttons
          @change.native="firstQuestionResult(hasCracklingNoises)"
          name="S12-first-question"
        />
      </b-form-group>
    </b-row>
    <b-row v-if="hasCracklingNoises == 'No'" class="triage-radio-question">
      <b-form-group
        label="Connect the handset to another port. Does this resolve the issue?"
      >
        <b-form-radio-group
          id="S12-Q2"
          v-model="worksOnOtherPort"
          :options="options"
          buttons
          @change.native="secondQuestionResult(worksOnOtherPort)"
          name="S12-second-question"
        />
      </b-form-group>
    </b-row>
  </div>
</template>
<script>
export default {
  data() {
    return {
      hasLooseConnection: "",
      hasCracklingNoises: "",
      hasOtherUsersExperienced: "",
      selectedCurlyCordModel: "",
      isServiceProvider: "",
      options: [
        { text: "Yes", value: "Yes" },
        { text: "No", value: "No" }
      ]
    };
  },
  methods: {
    firstQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$bvModal.show("sendEmailModal");
      }
    },
    secondQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$emit("show-solution-modal", "sendEmailModal");
      } else {
        this.$emit("show-solution-modal", "callITHelpdeskModal");
      }
    }
  }
};
</script>
<style scoped>
.triage-radio-question {
  color: white;
  justify-content: center;
  margin: 3%;
}

.modal-close-button {
  width: 50%;
  background-color: #576dc3;
}

.modal-proceed-button {
  width: 50%;
  background-color: rgb(147, 169, 255);
}

.modal-proceed-button-disabled {
  width: 50%;
  background-color: grey;
}

#orderCurlyCordModal .handset-model-dropdown {
  text-align: center;
  width: 70%;
}
</style>
