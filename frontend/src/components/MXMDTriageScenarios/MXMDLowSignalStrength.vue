<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Turn the handset off and on and click Proceed if the problem persists.">
                <b-button @click="didResetFix='No'">Proceed</b-button>
            </b-form-group>
        </b-row>
        <b-row v-if="didResetFix=='No'" class="triage-radio-question">
            <b-form-group label="Do you experience this problem only when you move around?">
                <b-form-radio-group
                id="S18-Q2"
                v-model="problemOccursWhenMoving"
                :options="options"
                buttons
                @change.native="secondQuestionResult(problemOccursWhenMoving)"
                name="S18-second-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="didResetFix=='No' && problemOccursWhenMoving=='No'" class="triage-radio-question">
            <b-form-group label="Do you experience this problem in a specific area of the building?">
                <b-form-radio-group
                id="S18-Q2"
                v-model="problemOccursInArea"
                :options="options"
                buttons
                @change.native="thirdQuestionResult(problemOccursInArea)"
                name="S18-second-question"/>
            </b-form-group>
        </b-row>     
        <b-row v-if="didResetFix=='No' && problemOccursWhenMoving=='No' && problemOccursInArea=='No'" class="triage-radio-question">
            <b-form-group label="Do other handsets or users in your area experience a similar problem?">
                <b-form-radio-group
                id="S18-Q2"
                v-model="occursInOtherHandsets"
                :options="options"
                buttons
                @change.native="fourthQuestionResult(occursInOtherHandsets)"
                name="S18-second-question"/>
            </b-form-group>
        </b-row>                 
    </div>
</template>
<script>
export default {
    data() {
        return {
            didResetFix: '',
            problemOccursWhenMoving: '',
            problemOccursInArea: '', 
            occursInOtherHandsets: '',  
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {

        secondQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'multipleHandsetModal')
            }
        },         
        thirdQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'multipleHandsetModal' )
            }
        },
        fourthQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'multipleHandsetModal' )
            }
            else {
                this.$emit('show-solution-modal', 'sendEmailModal' )
            }
        },  
    },
}
</script>
<style scoped>
.triage-radio-question { 
    color: white;     
    justify-content: center;
    margin: 3%;
}

.modal-close-button {
    width: 50%; 
    background-color: #576DC3;
}

.modal-proceed-button {
    width: 50%; 
    background-color: rgb(147, 169, 255);
}
</style>