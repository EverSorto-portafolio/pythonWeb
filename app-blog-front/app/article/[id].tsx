import { useRouter } from "next/router";
import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";

interface Article {
  id: number;
  title: string;
  content: string;
}

const ArticlePage = () => {
const [article, setArticle] = useState<Article | null>(null);
  const router = useRouter();
  const { id } = router.query;
  
  useEffect(() => {
    if(id){
        fetch( `http://127.0.0.1:5000/article/${id}`)
        .then(response => response.json())
        .then(data => setArticle(data))
        .catch(error => console.error("Error fetching articles:", error));
    }
  }, [id]);

  if(!article){
    return (
        <Layout>
            <div className="container mx-auto py-10">
               <p className="text-center"> Cargando articulo</p> 
            </div>
        </Layout>
    )
  }

  return (
    <Layout>
            <div className="container mx-auto py-10">
               <h1 className="text-4xl font-bold mb-6 text-indigo-600">
                {article.title}</h1>
                <p className="text-gray-700">{article.content}</p>
            </div>
        </Layout>
  )
    
}
export default ArticlePage;


  