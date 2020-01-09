<template>
  <b-container>
    <transition>
      <h5 class="h5 intro">
        This is a list of various How-To documents to assist those who seek
        technical, step-by-step guidance on configuring handsets.
      </h5>
    </transition>
    <div class="m-4">
      <transition>
        <b-row>
          <b-col class="px-4 handset-model-instruction"
            >Please select your handset model from below:</b-col
          >
          <b-col class="px-4 handset-model-help">
            <b-button
              v-b-modal.handsetModelHelpModal
              class="handset-model-help-link"
              variant="link"
              >How can I find my handset model?</b-button
            >
          </b-col>
        </b-row>
      </transition>
      <transition>
        <b-form-select
          class="handset-model-dropdown my-2"
          v-model="selectedHandsetType"
          :options="handsetOptions"
        ></b-form-select>
      </transition>
      <b-modal id="handsetModelHelpModal" size="lg" hide-footer hide-header>
        <div class="d-block p-5 modal-body-text">
          <p>
            You can usually locate the part number by turning the handset over
            and locating a white sticker with black text on the back of the
            handset. <br /><br />If your handset is not part of any of the
            series listed, please give our friendly staff a call on 123 456 and
            we'll assist you.
          </p>
        </div>
        <b-button
          class="my-5 mx-auto modal-close-button"
          block
          @click="$bvModal.hide('handsetModelHelpModal')"
        >
          Close
        </b-button>
      </b-modal>
      <div v-if="selectedHandsetType" class="select-question-dropdown">
        <transition>
          <b-row>
            <b-col class="px-4 handset-model-instruction"
              >Please choose from the following How-To instructions:</b-col
            >
            <b-col class="px-4 handset-model-help">
              <b-button
                v-b-modal.instructionHelpModal
                class="handset-model-help-link"
                variant="link"
                >What if these instructions don't address what I need?</b-button
              >
            </b-col>
          </b-row>
        </transition>
        <b-modal id="instructionHelpModal" size="lg" hide-footer hide-header>
          <div class="d-block p-5 modal-body-text">
            <p>
              You can call us, and a member of our friendly staff will assist
              you with your technical needs.
            </p>
          </div>
          <b-button
            class="my-5 mx-auto modal-close-button"
            block
            @click="$bvModal.hide('instructionHelpModal')"
          >
            Close
          </b-button>
        </b-modal>
        <transition>
          <b-form-select
            class="handset-symptom-dropdown my-2"
            v-model="selectedHowTo"
            :options="howToOptions"
          ></b-form-select>
        </transition>
      </div>
      <div>
        <instructions :howto="selectedHowTo" />
      </div>
      <div class="nav-buttons">
        <b-btn class="btn back-button" @click="$router.go(-1)">Back</b-btn>
      </div>
    </div>
  </b-container>
</template>
<script>
import howtoquestions from "../data/howtoquestions.json";
import handsets from "../data/handsets.json";
import Instructions from "../components/Instructions.vue";

export default {
  data() {
    return {
      handsetOptions: [
        { value: null, text: "Select your handset type" },
        { value: "MITEL330053", text: "Mitel 3300 53xx Series" },
        { value: "MITEL330069", text: "Mitel 3300 69xx Series" }
      ],
      selectedHandsetType: null,
      howToQuestions: howtoquestions,
      selectedHowTo: null
    };
  },
  computed: {
    howToOptions() {
      return this.howToQuestions["handsetType"][this.selectedHandsetType];
    }
  },
  components: {
    instructions: Instructions
  }
};
</script>
<style>
.btn.back-button {
  color: #a0fff5;
  background: none;
  border: none;
  bottom: 10%;
}

.btn.handset-model-help-link {
  font-size: 15px;
  color: #a0fff5;
  text-align: right;
}

.btn.handset-model-help-link:hover {
  color: azure;
}

.btn.back-button:hover,
.btn.proceed-button:hover {
  color: #a0fff5;
  background-color: #ffffff40;
  border: none;
}

.btn.back-button:active,
.btn.proceed-button:active {
  color: #a0fff5;
  background-color: #ffffff10;
  border: none;
}

.btn.back-button:focus,
.btn.proceed-button:focus {
  border: none;
}

.handset-model-dropdown {
  text-align: center;
  padding-left: 20%;
  padding-right: 20%;
}

.handset-model-help {
  text-align: right;
}

.handset-model-instruction {
  text-align: left;
  font-size: 15px;
  color: white;
  align-self: center;
}

#handsetModelHelpModal .modal-body-text {
  text-align: left;
}

#handsetModelHelpModal .modal-close-button {
  width: 50%;
  background-color: #576dc3;
}

.nav-buttons {
  bottom: 0px;
  text-align: center;
}

#instructionHelpModal .modal-body-text {
  text-align: left;
}

#instructionHelpModal .modal-close-button {
  width: 50%;
  background-color: #576dc3;
}

.handset-symptom-dropdown {
  text-align: center;
}

.intro {
  color: white;
  text-align: center;
  margin: 40px;
}

.select-question-dropdown {
  margin-top: 5%;
  margin-bottom: 5%;
}
/* Transitions */
.fade-view-enter-active,
.fade-view-leave-active {
  transition: opacity 1s;
}

.fade-view-enter,
.fade-view-leave-to {
  opacity: 0;
}
</style>
