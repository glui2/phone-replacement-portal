<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Does the handpiece rattle, or are there any loose parts or components inside the phone?">
                <b-form-radio-group
                id="S9-Q1"
                v-model="hasRattling"
                :options="options"
                buttons
                @change.native="damagedQuestionResult(hasRattling)"
                name="S9-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasRattling=='No'" class="triage-radio-question">
            <b-form-group label="Has the phone been dropped or physically damaged?">
                <b-form-radio-group
                id="S9-Q2"
                v-model="hasPhysicalDamage"
                :options="options"
                buttons
                @change.native="damagedQuestionResult(hasPhysicalDamage)"
                name="S9-second-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasRattling=='No' && hasPhysicalDamage=='No'" class="triage-radio-question">
            <b-form-group label="Test another phone in the same port as the faulty one. Are you getting the same fault?">
                <b-form-radio-group
                id="S9-Q3"
                v-model="anotherPhoneHasSameFault"
                :options="options"
                buttons
                @change.native="testAnotherPhoneResult(anotherPhoneHasSameFault)"
                name="S9-third-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasRattling=='No' && hasPhysicalDamage=='No' && anotherPhoneHasSameFault=='No'" class="triage-radio-question">
            <b-form-group label="Connect the faulty phone in a working port. Do you still have the same issue?">
                <b-form-radio-group
                id="S9-Q3"
                v-model="faultyInWorkingPort"
                :options="options"
                buttons
                @change.native="testWorkingPortResult(faultyInWorkingPort)"
                name="S9-third-question"/>
            </b-form-group>
        </b-row>                   
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasRattling: '',
            hasPhysicalDamage: '',
            anotherPhoneHasSameFault: '',
            options: [
                { text: 'Yes', value: 'Yes' },
                { text: 'No', value: 'No' }
            ]
        }
    },
    methods: {
        damagedQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$emit('show-solution-modal', 'notCoveredModal' )
            }
        },
        testAnotherPhoneResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$bvModal.show('callITHelpdeskModal')
            } 
        },
        testWorkingPortResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$bvModal.show('sendEmailModal')
            }
            else {
                this.$bvModal.show('callITHelpdeskModal')
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

.modal-close-button {
    width: 50%; 
    background-color: #576DC3;
}

.modal-proceed-button {
    width: 50%; 
    background-color: rgb(147, 169, 255);
}
</style>