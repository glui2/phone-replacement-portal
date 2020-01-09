<template>
  <div style="text-align: center">
    <b-row class="triage-radio-question">
      <b-form-group
        label="Restart the system and click proceed if this does not fix the issue."
      >
        <b-button @click="didRestartFail = 'Yes'">Proceed</b-button>
      </b-form-group>
    </b-row>
    <b-row v-if="didRestartFail == 'Yes'" class="triage-radio-question">
      <b-form-group label="Is XXX your carrier or service provider?">
        <b-form-radio-group
          id="S4-Q2"
          v-model="isXxxProvider"
          :options="Options"
          buttons
          @change.native="secondQuestionResult(isXxxProvider)"
          name="S4-second-question"
        />
      </b-form-group>
    </b-row>
    <b-modal id="callServiceProvider" size="lg" hide-footer hide-header>
      <div class="d-block p-5 modal-body-text">
        <p>Please call your service provider to report a fault.</p>
      </div>
      <b-button
        class="my-5 mx-auto modal-close-button"
        block
        @click="$bvModal.hide('callServiceProvider')"
      >
        Close
      </b-button>
    </b-modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      didRestartFail: "",
      isXxxProvider: "",
      restartOptions: [{ text: "Proceed", value: "Proceed" }],
      Options: [
        { text: "Yes", value: "Yes" },
        { text: "No", value: "No" }
      ]
    };
  },
  methods: {
    secondQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$emit("show-solution-modal", "callLineFault");
      } else {
        this.$bvModal.show("callServiceProvider");
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
</style>
