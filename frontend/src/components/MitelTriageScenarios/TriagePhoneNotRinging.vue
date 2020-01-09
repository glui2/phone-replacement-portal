<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Has the handset been dropped?">
                <b-form-radio-group
                id="S8-Q1"
                v-model="hasBeenDropped"
                :options="options"
                buttons
                @change.native="firstQuestionResult(hasBeenDropped)"
                name="S8-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasBeenDropped=='No'" class="triage-radio-question">
            <b-form-group label="Does the handset flash when called?">
                <b-form-radio-group
                id="S8-Q2"
                v-model="doesHandsetFlash"
                :options="options"
                buttons
                @change.native="secondQuestionResult(doesHandsetFlash)"
                name="S8-second-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasBeenDropped=='No' && doesHandsetFlash=='Yes'" class="triage-radio-question">
            <b-form-group label="Press the 'Up' arrow key while the handset is flashing to increase the ringer volume. If this does not solve the issue, press Proceed below.">
                <b-button @click="handsetVolumeNotMuted = 'Yes'">Proceed</b-button>
            </b-form-group>
        </b-row>
        <b-row v-if="hasBeenDropped=='No' && doesHandsetFlash=='Yes' && handsetVolumeNotMuted=='Yes'" class="triage-radio-question">
            <b-form-group label="Plug the faulty phone into a different working port and test by calling it and checking the ringer volume as per the previous step. Is there any change in behaviour?">
                <b-form-radio-group
                id="S8-Q4"
                v-model="worksInDifferentPort"
                :options="options"
                buttons
                @change.native="fourthQuestionResult(worksInDifferentPort)"
                name="S8-fourth-question"/>
            </b-form-group>
        </b-row>                                   
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasBeenDropped: '',
            doesHandsetFlash: '',
            handsetVolumeNotMuted: '',
            worksInDifferentPort: '', 
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ],
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
        },
        secondQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "No"){
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
        },
        fourthQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'callITHelpdeskModal' )
            }
            else {
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
        }
    },
}
</script>
<style scoped>
.triage-radio-question { 
    color: white;     
    justify-content: center;
    margin: 3%;
}
</style>