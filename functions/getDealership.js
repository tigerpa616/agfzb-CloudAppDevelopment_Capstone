/**
 * Get all dealerships
 */

 const Cloudant = require('@cloudant/cloudant');


 async function main(params) {
     const cloudant = Cloudant({
         url: "https://f29fb6c8-981f-4cc0-b09b-9cca05f47b9d-bluemix.cloudantnosqldb.appdomain.cloud",
         plugins: { iamauth: { iamApiKey: "Un0dOUFr88tJze2BpfAveXsLYYozRoAKN6a8zLiXz-EC" } }
     });
 
 
     try {
         //selecting cloudant dbs
         const db = cloudant.db.use("dealerships");
          let dbList = await db.list({include_docs:true});
         return { "dbs": dbList };
         
         
     } catch (error) {
         return { error: error.description };
     }
 
 }
