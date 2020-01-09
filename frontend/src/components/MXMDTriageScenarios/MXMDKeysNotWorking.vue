<template>
    <div style="text-align: center">
        <b-row class="triage-radio-question">
            <b-form-group label="Restart the phone if you haven't done so already. If this did not resolve the issue, click Proceed  and place a request for a replacement handset using the order form.">
                <b-button to="/orderreplacement">Proceed</b-button>
            </b-form-group>
        </b-row>   
    </div>
</template>

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
</style>