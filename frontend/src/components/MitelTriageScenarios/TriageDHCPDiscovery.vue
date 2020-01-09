<template>
  <div style="text-align: center">
    <b-row class="triage-radio-question">
      <b-form-group
        label="Is the wall socket or port where the phone is connected activated as a voice port?"
      >
        <b-form-radio-group
          id="S10-Q1"
          v-model="activatedAsVoicePort"
          :options="options"
          buttons
          @change.native="firstQuestionResult(activatedAsVoicePort)"
          name="S3-first-question"
        />
      </b-form-group>
    </b-row>
    <b-row v-if="activatedAsVoicePort == 'Yes'" class="triage-radio-question">
      <b-form-group
        label="Plug the faulty phone in another port where there is a working handset. Does this fix the issue?"
      >
        <b-form-radio-group
          id="S10-Q1"
          v-model="worksInAnotherPort"
          :options="options"
          buttons
          @change.native="secondQuestionResult(worksInAnotherPort)"
          name="S10-second-question"
        />
      </b-form-group>
    </b-row>
    <b-modal id="callSupportModal" size="lg" hide-footer hide-header>
      <div class="d-block p-5 modal-body-text">
        <p>
          Please call us for support and one of our friendly staff will assist
          you.
        </p>
      </div>
      <b-button
        class="my-5 mx-auto modal-close-button"
        block
        @click="$bvModal.hide('callSupportModal')"
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
      activatedAsVoicePort: "",
      worksInAnotherPort: "",
      options: [
        { text: "Yes", value: "Yes" },
        { text: "No", value: "No" }
      ]
    };
  },
  methods: {
    firstQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "No") {
        this.$emit("show-solution-modal", "callITHelpdeskModal");
      }
    },
    secondQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$emit("show-solution-modal", "callITHelpdeskModal");
      } else {
        this.$bvModal.show("callSupportModal");
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
