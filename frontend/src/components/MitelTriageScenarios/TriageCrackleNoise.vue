<template>
  <div style="text-align: center">
    <b-row class="triage-radio-question">
      <b-form-group
        label="Check the port on the back of the phone. Is there any damage or loose connections?"
      >
        <b-form-radio-group
          id="S1-Q1"
          v-model="hasLooseConnection"
          :options="options"
          buttons
          @change.native="firstQuestionResult(hasLooseConnection)"
          name="S1-first-question"
        />
      </b-form-group>
    </b-row>
    <b-row v-if="hasLooseConnection == 'No'" class="triage-radio-question">
      <b-form-group
        label="While on a phone call, wiggle the curly cord. Does this create any crackling noises?"
      >
        <b-form-radio-group
          id="S1-Q2"
          v-model="hasCracklingNoises"
          :options="options"
          buttons
          @change.native="secondQuestionResult(hasCracklingNoises)"
          name="S1-second-question"
        />
      </b-form-group>
    </b-row>
    <b-row
      v-if="hasCracklingNoises == 'No' && hasLooseConnection == 'No'"
      class="triage-radio-question"
    >
      <b-form-group
        label="Has this problem has been experienced by other users on site?"
      >
        <b-form-radio-group
          id="S1-Q3"
          v-model="hasOtherUsersExperienced"
          :options="options"
          buttons
          @change.native="thirdQuestionResult(hasOtherUsersExperienced)"
          name="S1-third-question"
        />
      </b-form-group>
    </b-row>
    <b-row
      v-if="
        hasCracklingNoises == 'No' &&
          hasLooseConnection == 'No' &&
          hasOtherUsersExperienced == 'Yes'
      "
      class="triage-radio-question"
    >
      <b-form-group label="Is xxx your service provider?">
        <b-form-radio-group
          id="S1-Q4"
          v-model="isXxxServiceProvider"
          :options="options"
          buttons
          @change.native="fourthQuestionResult(isXxxServiceProvider)"
          name="S1-fourth-question"
        />
      </b-form-group>
    </b-row>
    <b-modal id="orderCurlyCordModal" size="lg" hide-footer hide-header>
      <div class="d-block p-5 modal-body-text">
        <p>
          The handpiece and curly cord is faulty. Select the colour of your
          curly cord, click <strong>proceed</strong> and place a request for a
          replacement handpiece using the order form.
        </p>
      </div>
      <b-form-select
        class="handset-model-dropdown my-2"
        v-model="selectedCurlyCordModel"
        :options="curlyCordOptions"
      ></b-form-select>
      <b-button
        v-if="selectedCurlyCordModel"
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
        v-else
        class="my-5 mx-auto modal-proceed-button-disabled"
        block
        disabled
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
      hasLooseConnection: "",
      hasCracklingNoises: "",
      hasOtherUsersExperienced: "",
      selectedCurlyCordModel: "",
      isXxxServiceProvider: "",
      options: [
        { text: "Yes", value: "Yes" },
        { text: "No", value: "No" }
      ],
      curlyCordOptions: [
        { text: "Almond", value: "Almond Curly Cord - CCT0133 RFB" },
        { text: "Black", value: "Black Curly Cord - CCT0132 RFB" },
        { text: "Burgundy", value: "Burgundy Curly Cord - CCT0134 RFB" },
        { text: "Grey", value: "Grey Curly Cord - CCT0192 RFB" },
        { text: "White", value: "White Curly Cord - CCT0073 RFB" }
      ]
    };
  },
  methods: {
    firstQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$emit("show-solution-modal", "notCoveredModal");
      }
    },
    secondQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "Yes") {
        this.$bvModal.show("orderCurlyCordModal");
      }
    },
    thirdQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "No") {
        this.$emit("show-solution-modal", "sendEmailModal");
      }
    },
    fourthQuestionResult(selectedRadioButton) {
      if (selectedRadioButton == "No") {
        this.$emit("show-solution-modal", "callServiceProviderModal");
      } else {
        this.$emit("show-solution-modal", "callLineFault");
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
