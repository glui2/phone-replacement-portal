<template>
  <div style="text-align: center">
    <b-row class="triage-radio-question">
      <b-form-group label="Does the handset work if you use another charger?">
        <b-form-radio-group
          id="S17-Q1"
          v-model="worksWithOtherCharger"
          :options="options"
          buttons
          @change.native="firstQuestionResult(worksWithOtherCharger)"
          name="S17-first-question"
        />
      </b-form-group>
    </b-row>
    <b-row v-if="worksWithOtherCharger == 'No'" class="triage-radio-question">
      <b-form-group
        label="Does it work if you swap your battery with a working phone of a similar model?"
      >
        <b-form-radio-group
          id="S17-Q2"
          v-model="worksWithOtherBattery"
          :options="options"
          buttons
          @change.native="secondQuestionResult(worksWithOtherBattery)"
          name="S17-second-question"
        />
      </b-form-group>
    </b-row>
    <b-modal id="orderCurlyCordModal" size="lg" hide-footer hide-header>
      <div class="d-block p-5 modal-body-text">
        <p>
          You will need to replace your {{ replacementPart }}. Click
          <strong>Proceed</strong> below to continue to the Order Replacement
          Handset page, where you can send a request for a replacement
          {{ replacementPart }} to the faults team.
        </p>
      </div>
      <b-button
        class="my-5 mx-auto modal-proceed-button"
        block
        :to="{
          name: 'Order Specified Replacement Part',
          params: { partNumberProp: this.selectedCurlyCordModel }
        }"
      >
        Proceed
      </b-button>
      <b-button
        class="my-5 mx-auto modal-close-button"
        block
        @click="$bvModal.hide('orderCurlyCordModal')"
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
      worksWithOtherCharger: "",
      worksInAnotherPort: "",
      replacementPart: "",
      options: [
        { text: "Yes", value: "Yes" },
        { text: "No", value: "No" }
      ]
    };
  },
  methods: {
    firstQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.replacementPart = "charger";
        this.$bvModal.show("orderCurlyCordModal");
      }
    },
    secondQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.replacementPart = "battery";
        this.$bvModal.show("orderCurlyCordModal");
      } else {
        this.replacementPart = "handset";
        this.$bvModal.show("orderCurlyCordModal");
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
