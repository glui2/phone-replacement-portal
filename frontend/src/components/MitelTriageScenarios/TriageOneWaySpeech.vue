<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Does the handpiece rattle, or are there any loose parts or components inside the phone?">
                <b-form-radio-group
                id="S5-Q1"
                v-model="hasRattling"
                :options="options"
                buttons
                @change.native="damagedQuestionResult(hasRattling)"
                name="S5-first-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasRattling=='No'" class="triage-radio-question">
            <b-form-group label="Has the phone been dropped or physically damaged?">
                <b-form-radio-group
                id="S5-Q2"
                v-model="hasPhysicalDamage"
                :options="options"
                buttons
                @change.native="damagedQuestionResult(hasPhysicalDamage)"
                name="S5-second-question"/>
            </b-form-group>
        </b-row>
        <b-row v-if="hasRattling=='No' && hasPhysicalDamage=='No'" class="triage-radio-question">
            <b-form-group label="Replace the handpiece and curly cord with the handpiece from another handset - does that resolve the issue?">
                <b-form-radio-group
                id="S5-Q3"
                v-model="hasFaultyHandpiece"
                :options="options"
                buttons
                @change.native="testHandpieceQuestionResult(hasFaultyHandpiece)"
                name="S5-third-question"/>
            </b-form-group>
        </b-row>
        <b-modal id="replaceFaultyHandpiece" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>The handpiece and curly cord is faulty. <br/> Click <strong>proceed</strong> and place a request for a replacement handpiece using the order form.</p>
            </div>
            <b-button class="my-5 mx-auto modal-proceed-button" block to="/orderreplacement" > Proceed </b-button>             
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('replaceFaultyHandpiece')"> Close </b-button>
        </b-modal>
        <b-modal id="replaceFaultyHandset" size="lg" hide-footer hide-header> 
            <div class="d-block p-5 modal-body-text">
                <p>The handset may be faulty. <br/> Click <strong>proceed</strong> and place a request for a replacement handset using the order form.</p>
            </div> 
            <b-button class="my-5 mx-auto modal-proceed-button" block to="/orderreplacement" > Proceed </b-button>             
            <b-button class="my-5 mx-auto modal-close-button" block @click="$bvModal.hide('replaceFaultyHandset')"> Close </b-button>
        </b-modal>               
    </div>
</template>
<script>
export default {
    data() {
        return {
            hasRattling: '',
            hasPhysicalDamage: '',
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
        testHandpieceQuestionResult(selectedRadioButton){
            if (selectedRadioButton == "Yes"){
                this.$bvModal.show('replaceFaultyHandpiece')
            } 
            else {
                this.$bvModal.show('replaceFaultyHandset')
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