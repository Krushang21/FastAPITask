import * as Yup from 'yup';
export const AddProductSchema = Yup.object().shape({
    title: Yup.string().min(3, "Product title must be at least 3 characters long").required("Please Enter Title"),
    content: Yup.string().min(3, "Product content    must be at least 3 characters long").required("Please Enter Title"),
    

});
