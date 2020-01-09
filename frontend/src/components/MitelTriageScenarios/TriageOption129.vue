<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Is the port (wall socket where the phone is connected) activated as a voiceport?">
                <b-form-radio-group
                id="S6-Q1"
                v-model="isPortActivated"
                :options="options"
                buttons
                @change.native="firstQuestionResult(isPortActivated)"
                name="S6-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="isPortActivated=='Yes'" class="triage-radio-question">
            <b-form-group label="Plug the faulty phone into another port where there is a working handset - does the phone register and operate as usual?">
                <b-form-radio-group
                id="S6-Q2"
                v-model="doesPhoneAppear"
                :options="options"
                buttons
                @change.native="secondQuestionResult(doesPhoneAppear)"
                name="S6-second-question"/>
            </b-form-group>
        </b-row>                 
    </div>
</template>
<script>
export default {
    data() {
        return {
            isPortActivated: '',
            doesPhoneAppear: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "No"){
                this.$emit('show-solution-modal', 'callITHelpdeskModal' )
            }
        },
        secondQuestionResult(selectedRadioButton){
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