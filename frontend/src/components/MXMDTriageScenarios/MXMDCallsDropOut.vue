<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Has anybody else in your environment experienced a similar issue?">
                <b-form-radio-group
                id="S20-Q1"
                v-model="haveOthersExperienced"
                :options="options"
                buttons
                @change.native="firstQuestionResult(haveOthersExperienced)"
                name="S20-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="haveOthersExperienced=='No'" class="triage-radio-question">
            <b-form-group label="Plug in another working handset into the port. Does the handset work?">
                <b-form-radio-group
                id="S20-Q2"
                v-model="doesOtherHandsetWork"
                :options="options"
                buttons
                @change.native="secondQuestionResult(doesOtherHandsetWork)"
                name="S20-second-question"/>
            </b-form-group>
        </b-row>       
    </div>
</template>
<script>
export default {
    data() {
        return {
            haveOthersExperienced: '',
            doesOtherHandsetWork: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        firstQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'callITHelpdeskModal' )
            }
        },
        secondQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "No"){
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